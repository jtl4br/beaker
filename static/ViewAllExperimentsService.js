angular.module('myApp').factory('ViewAllExperimentsService',
['$timeout', '$http', '$q', function ($timeout, $http, $q) {
    var selectedExperiment;

    function getAllExperiments() {
        return $http.get('/api/Experiment').then(function(response) {
            console.log(response);
            return response;
        });
    }
    function getExperiment(username) {
        var defer = $q.defer();
        $http.get('/api/Experiment', {params: {username: username}})
        .success(function (data) {
            defer.resolve(data);
        })
        .error(function(data,status) {
            defer.reject("Get experiment error");
            // console.error("Get experiment Error", status, data);
        });
        return defer.promise;
    }

    function getSelectedExperiment() {
        // FIXME: Code for sample data, not live data.
        return selectedExperiment;
    }

    function setSelectedExperiment(experiment) {
        // FIXME: Code for sample data, not live data.
        selectedExperiment = experiment;
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
        updateExperiment: updateExperiment,
        getAllExperiments: getAllExperiments,
        getSelectedExperiment: getSelectedExperiment,
        setSelectedExperiment: setSelectedExperiment
    });
}]);

