angular.module('myApp').factory('ExperimentService',
['$timeout', '$http', '$q', function ($timeout, $http, $q) {

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
        getExperiment: getExperiment,
        updateExperiment: updateExperiment
    });
}]);

