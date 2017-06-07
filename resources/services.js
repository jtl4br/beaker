angular.module('myApp').factory('UserService',
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

    function getExperiment(username) {
        return $http.get('/api/Experiment', {params: {username: username}})
        .success(function (data) {
            return data;
        })
        .error(function(data,status) {
            console.error("Get experiment Error", status, data);
        });
    }

    function updateExperiment(username, major_name, year) {
        return $http.put('/api/Student', {username: username, major_name: major_name, year: year})
        .success(function (data) {
            return data;
        })
        .error(function(data,status) {
            console.error("Update Student Error", status, data);
        });
    }

    return ({
        authenticate: authenticate,
        register: register,
        getUser: getUser,
        logout: logout,
        isLoggedIn: isLoggedIn,
        getExperiment: getExperiment,
        updateExperiment: updateExperiment
    });
}]);

