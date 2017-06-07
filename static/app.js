var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function ($routeProvider) {
    $routeProvider
    //Login Partials
    .when('/', {
        templateUrl: 'static/partials/login.html',
        controller: 'loginController'
    })
    .otherwise({
        redirectTo: '/'
    });
})
.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('//').endSymbol('//');
}]);
