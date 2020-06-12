import "../util/request.dart";

class homeScreenAPI {
  static const String path = "/knowledgegraph"; // should be /home, /knowledge graph is only for testing

  static Future<Map<String, dynamic>> getHomeScreen(Map<String, dynamic> params) {
    var client = HttpService.getConstructor(homeScreenAPI.path, params);
    return client.getResponse();
  } 

}