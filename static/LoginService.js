angular.module('myApp').factory('LoginService',
['$timeout', '$http', '$q', function ($timeout, $http, $q) {

    var user = null;
    var isLoggedIn = false;

    function getUser() {
        return user;
    }

    function logout() {
        var deferred = $q.defer();
        user = null;
        isLoggedIn = false;
        deferred.resolve("Logged Out");
        return deferred.promise;
    }

    function authenticate(username, password) {
        //http://twisted.readthedocs.io/en/twisted-16.2.0/core/howto/defer-intro.html
        //See above on deffereds for async code

        //Post request to server
        return $http.post('/api/AuthenticateUser', {username: username, password: password})
        .success(function(data) {
            user = data.username;
            isLoggedIn = true;
            return data;
        })
        .error(function(data, status) {
            console.error("Authenticate User Error", status, data);
        });
    }

    return ({
        authenticate: authenticate,
        getUser: getUser,
        logout: logout,
        isLoggedIn: isLoggedIn
    });
}]);

