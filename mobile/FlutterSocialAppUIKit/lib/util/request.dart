import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart';

HttpClient client = new HttpClient();

const authority = "123.56.73.194:3389";

Future<Response> fetchData(path, params) {
  var uri = Uri.http(authority, path, params);
  return get(uri);
}

class HttpService {
  String path;
  Map<String, dynamic> params;
  Map<String, dynamic> body;

  HttpService.getConstructor(this.path, this.params);
  HttpService.postConstructor(this.path, this.body);
  HttpService.defaultConstructor(this.path);

  Future<Map<String, dynamic>> getResponse() async {
    var uri = Uri.http(authority, path, params);
    Response res = await get(uri);

    if (res.statusCode == 200) {
      Map<String, dynamic> body = jsonDecode(res.body);

      return body;
    } else {
      throw "Response Error";
    }
  }

  Future<void> postRequest() async {
    var uri = Uri.http(authority, path);
    Response res = await post(
      uri,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(this.body)
    );

    if (res.statusCode == 200) {
      Map<String, dynamic> body = jsonDecode(res.body);

      return body;
    } else {
      throw "Response Error";
    }
  }
}
