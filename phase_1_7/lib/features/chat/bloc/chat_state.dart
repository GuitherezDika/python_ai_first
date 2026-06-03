import 'package:equatable/equatable.dart';

abstract class ChatState extends Equatable {
  @override
  List<Object?> get props => [];
}

class ChatInitial extends ChatState {}

// sedang streaming ; AI sedang mengetik
class ChatStreaming extends ChatState {
  final String currentText;
  ChatStreaming(this.currentText);

  @override
  List<Object?> get props => [currentText];
}

// streaming selesai
class ChatDone extends ChatState {
  final String finalText;
  ChatDone(this.finalText);

  @override
  List<Object?> get props => [finalText];
}

// error
class ChatError extends ChatState {
  final String message;
  ChatError(this.message);

  @override
  List<Object?> get props => [message];
}
