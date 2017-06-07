var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function ($routeProvider) {
    $routeProvider
    //Login Partials
    .when('/', {
        templateUrl: 'static/partials/login.html',
        controller: 'loginController'
    })
    .when('/experiments', {
        templateUrl: 'static/partials/experiments.html',
        controller: 'experimentController'
    })
    .otherwise({
        redirectTo: '/'
    });
})
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('//').endSymbol('//');
}]);
