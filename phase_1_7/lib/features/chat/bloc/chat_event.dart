import 'package:equatable/equatable.dart';

abstract class ChatEvent extends Equatable {
  @override
  List<Object?> get props => [];
}

// user kirim pesan dengan klik tombol SEND
class SendMessageEvent extends ChatEvent {
  final String message;
  SendMessageEvent(this.message);

  @override
  List<Object?> get props => [message];
}

// chunk baru datang dari backend
class ChunkReceivedEvent extends ChatEvent {
  final String chunk;
  ChunkReceivedEvent(this.chunk);

  @override
  List<Object?> get props => [chunk];
}

// streaming selesai (backend kirim [DONE])
class StreamDoneEvent extends ChatEvent {}
