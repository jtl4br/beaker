angular.module('myApp').controller('loginController',
  ['$scope', '$location', 'LoginService',
  function ($scope, $location, LoginService) {
    $scope.username = 'user';

    $scope.authenticate = function () {

      // initial values
      $scope.error = false;
      $scope.disabled = true;

      if ($scope.loginForm.username === null) {
        $scope.error = true;
        $scope.errorMessage = "Needs a username";
        return;
      }
      if ($scope.loginForm.password === null) {
        $scope.error = true;
        $scope.errorMessage = "Needs a password";
        return;
      }

      // call login from service
      LoginService.authenticate($scope.loginForm.username, $scope.loginForm.password)
        // handle success
        .then(function (data) {
          //$location.path('/main');
          console.log(data);
          console.log(data.data);
          if (data.data) {
            // redirect to main page depending on type
            console.log("REDIRECTING");
            $location.path('/experiments');
            $scope.loginForm = {};
          } else {
            console.log("AUTH FAILED");
            $scope.error = true;
            $scope.errorMessage = "Invalid username and/or password";
            $scope.loginForm = {};
          }
        });
    };
}])
