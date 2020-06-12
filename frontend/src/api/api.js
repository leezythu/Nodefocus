import request from "@/utils/request";

export function postCount() {
  return request({
    url: "/count/",
    method: "post"
  });
}

export function getFields() {
  return request({
    url: "/fields",
    method: "get"
  });
}

// query would look like "fieldname/?limit=100"
export function getFieldDetails(query, params) {
  return request({
    url: "/fields/" + query,
    method: "get",
    params: params
  });
}

export function getPersonalDetails(params) {
  return request({
    url: "/person/",
    method: "get",
    params: params
  });
}

export function getNews(params) {
  return request({
    url: "/news/",
    method: "get",
    params: params
  });
}
