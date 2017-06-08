angular.module('myApp').factory('CreateExperimentService',
['$timeout', '$http', '$q', function ($timeout, $http, $q) {

    function postExperiment(name, card, target, start_date, end_date, age_l, age_u) {
        return $http.post('/api/Experiment', 
            {name:name, card:card, target:target,
                start_date:start_date,end_date:end_date,
                age_l:age_l,age_u:age_u}
            ).then(function(response) {
            console.log(response)
            return response;
        });
    }

    return ({
        postExperiment:postExperiment
    });    
}]);