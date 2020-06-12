import { login, logout, getInfo, signup } from '@/api/user';
import { asyncRoutes, constantRoutes } from '@/router';

const md5 = require('js-md5');

const state = {
    token: '',
    name: '',
    avatar: '',
    permission: '',
    routes: []
};

const mutations = {
    SET_TOKEN: (state, token) => {
        state.token = token;
    },
    SET_NAME: (state, name) => {
        state.name = name;
    },
    SET_AVATAR: (state, avatar) => {
        state.avatar = avatar;
    },
    SET_PERMISSION: (state, permission) => {
        state.permission = permission;
    },
    SET_ROUTES: (state, routes) => {
        state.routes = constantRoutes.concat(routes);
    }
};

/**
 * Use meta.role to determine if the current user has permission
 * @param roles
 * @param route
 */
function hasPermission(roles, route) {
    if (route.meta && route.meta.roles) {
        return roles.some(role => route.meta.roles.includes(role));
    } else {
        return true;
    }
}

/**
   * Filter asynchronous routing tables by recursion
   * @param routes asyncRoutes
   * @param roles
   */
function filterAsyncRoutes(routes, roles) {
    const res = [];

    routes.forEach(route => {
        const tmp = { ...route };
        if (hasPermission(roles, tmp)) {
            if (tmp.children) {
                tmp.children = filterAsyncRoutes(tmp.children, roles);
            }
            res.push(tmp);
        }
    });
    return res;
}

const actions = {
    // user login
    login({ commit }, userInfo) {
        const { username, password } = userInfo;

        return new Promise((resolve, reject) => {
            return login({ username: username.trim(), password: md5(password) }).then(response => {
                const { payload } = response;
                commit('SET_TOKEN', payload.token);
                commit('SET_NAME', payload.username);
                commit('SET_AVATAR', payload.avatar);
                commit('SET_PERMISSION', payload.permission);
                const permissionRoutes = filterAsyncRoutes(asyncRoutes, [payload.permission]);
                commit('SET_ROUTES', permissionRoutes);
                resolve();
            }).catch(error => {
                reject(error);
            });
        });
    },

    // user signup
    signup({ commit }, userInfo) {
        const { username, password, email } = userInfo;
        return new Promise((resolve, reject) => {
            return signup({ username: username.trim(), password: md5(password), email: email }).then(response => {
                // const { data } = response;
                // commit('SET_TOKEN', data.token);
                // setToken(data.token);
                resolve();
            }).catch(error => {
                reject(error);
            });
        });
    },

    // get user info
    getInfo({ commit, state }) {
        return new Promise((resolve, reject) => {
            getInfo(state.token).then(response => {
                console.log(response);
                const { payload } = response;

                if (!payload) {
                    reject('Verification failed, please Login again.');
                }

                const { username, avatar } = payload;

                commit('SET_NAME', username);
                commit('SET_AVATAR', avatar);
                resolve(payload);
            }).catch(error => {
                reject(error);
            });
        });
    },

    // user logout
    async logout({ commit, state }) {
        return new Promise((resolve, reject) => {
            logout(state.token).then(() => {
                commit('SET_TOKEN', '');
                commit('SET_AVATAR', '');
                commit('SET_NAME', '');
                commit('SET_PERMISSION', '');
                // resetRouter();
                resolve();
            }).catch(error => {
                reject(error);
            });
        });
    },

    // remove token
    resetToken({ commit }) {
        return new Promise(resolve => {
            commit('SET_TOKEN', '');
            commit('SET_AVATAR', '');
            commit('SET_NAME', '');
            commit('SET_PERMISSION', '');
            resolve();
        });
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    actions
};

