import 'package:web_socket_channel/web_socket_channel.dart';

class ChatWebsocket {
  static const String _url = 'ws://192.168.73.94:8000/ws/chat';
  WebSocketChannel? _channel;

  void connect() {
    _channel = WebSocketChannel.connect(Uri.parse((_url)));
  }

  void sendMessage(String message) {
    _channel?.sink.add(message);
  }

  Stream<String> get messageStream {
    return _channel!.stream.map((data) => data.toString());
  }

  void disconnect() {
    _channel?.sink.close();
    _channel = null;
  }
}
