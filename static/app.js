var myApp = angular.module('myApp',['ngRoute']);

myApp.config(function ($routeProvider) {
    $routeProvider
    //Login Partials
    .when('/', {
        templateUrl: 'static/partials/login.html',
        controller: 'loginController'
    })
    .when('/experiments', {
        templateUrl: 'static/partials/viewAllExperiments.html',
        controller: 'viewAllExperimentsController'
    })
    .when('/view', {
        templateUrl: 'static/partials/viewExperiment.html',
        controller: 'viewExperimentController'

    .when('/experiments/create', {
        templateUrl: 'static/partials/createExperiment.html',
        controller: 'createExperimentController'

    })
    .otherwise({
        redirectTo: '/'
    });
});
