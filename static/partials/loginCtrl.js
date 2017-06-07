angular.module('myApp').controller('loginController',
  ['$scope', '$location', 'UserService',
  function ($scope, $location, UserService) {
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
      UserService.authenticate($scope.loginForm.username, $scope.loginForm.password)
        // handle success
        .success(function (data) {
          //$location.path('/main');
          if (data) {
            // redirect to main page depending on type
            if (data.userType == "Student") {
              $location.path('/main');
            }
            $location
            $scope.loginForm = {};
          } else {
            $scope.error = true;
            $scope.errorMessage = "Invalid username and/or password";
            $scope.loginForm = {};
          }
        });
    };
}])
