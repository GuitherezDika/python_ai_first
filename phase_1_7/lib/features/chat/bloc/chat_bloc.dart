import 'package:flutter_bloc/flutter_bloc.dart';
import '../data/chat_websocket.dart';
import 'chat_event.dart';
import 'chat_state.dart';

class ChatBloc extends Bloc<ChatEvent, ChatState> {
  final ChatWebsocket _ws = ChatWebsocket();
  String _accumulatedText = ''; // kumpulan chunk yang masuk

  ChatBloc() : super(ChatInitial()) {
    // connect ke backend saat BLoC dibuat
    _ws.connect();

    // listen stream dari WebSocket
    _ws.messageStream.listen(
      (data) {
        if (data == '[DONE]') {
          add(StreamDoneEvent());
        } else {
          add(ChunkReceivedEvent(data));
        }
      },
      onError: (error) {
        emit(ChatError(error.toString()));
      },
    );

    // handle event kirim pesan
    on<SendMessageEvent>((event, emit) {
      _accumulatedText = '';
      _ws.sendMessage(event.message);
      emit(ChatStreaming(''));
    });

    // handle chunk baru masuk
    on<ChunkReceivedEvent>((event, emit) {
      _accumulatedText += event.chunk;
      emit(ChatStreaming(_accumulatedText));
    });

    // handle streaming selesai
    on<StreamDoneEvent>((event, emit) {
      emit((ChatDone(_accumulatedText)));
    });
  }

  @override
  Future<void> close() {
    _ws.disconnect();
    return super.close();
  }
}
