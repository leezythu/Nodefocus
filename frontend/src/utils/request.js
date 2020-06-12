import axios from "axios";
// import store from '@/store';
// import { Message } from 'element-ui';

// create an axios instance
const service = axios.create({
  baseURL: "http://127.0.0.1:5000/", //"http://123.56.73.194:3389/", // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 100000 // request timeout
});

// console.log(process.env.VUE_APP_BASE_API)
// console.log("http://101.200.241.8:3389/")

// request interceptor
service.interceptors.request.use(
  config => {
    // do something before request is sent
    // config.headers['Content-Type'] = 'application/json;charset=UTF-8';
    // if (store.getters.token) {
    //     // let each request carry token
    //     // ['X-Token'] is a custom headers key
    //     // please modify it according to the actual situation
    //     config.headers['X-ACCESS-TOKEN'] = store.getters.token;
    //     config.headers['X-ACCESS-USERNAME'] = store.getters.name;
    // }
    return config;
  },
  error => {
    // do something with request error
    console.log(error); // for debug
    return Promise.reject(error);
  }
);

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
   */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    const res = response.data;
    // if the custom status is not 200, it is judged as an error.
    // console.log(res.status);
    // if (res.status !== 200) {
    //     // if (res.status === 401) {
    //     //     // to re-login
    //     //     MessageBox.confirm('You have been logged out, please log in again', 'Error', {
    //     //         confirmButtonText: 'Re-Login',
    //     //         type: 'error',
    //     //         showCancelButton: false
    //     //     }).then(() => {
    //     //         store.dispatch('user/resetToken').then(() => {
    //     //             location.reload();
    //     //         });
    //     //     });
    //     // } else {
    //         if (res.status === 423 || res.status === 404) {
    //             Message({
    //                 message: res.message,
    //                 type: 'warning',
    //                 duration: 5 * 1000
    //             });
    //         } else {
    //             Message({
    //                 message: res.message || 'Error',
    //                 type: 'error',
    //                 duration: 5 * 1000
    //             });
    //         }
    //     // }
    //     return Promise.reject(new Error(res.message || 'Error'));
    // } else {
    return res;
    // }
  },
  error => {
    console.log("err" + error); // for debug
    // Message({
    //     message: error.message,
    //     type: 'error',
    //     duration: 5 * 1000
    // });
    return Promise.reject(error);
  }
);

export default service;
