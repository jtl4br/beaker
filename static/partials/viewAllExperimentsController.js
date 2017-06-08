angular.module('myApp').controller('viewAllExperimentsController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ($scope, $location, ViewAllExperimentsService) {
		$scope.experiments = [];
		ViewAllExperimentsService.getAllExperiments().then(function(x){
			$scope.experiments = x;
			// console.log($scope.experiments);
			for (var i = 0; i < 2; i++){
				// console.log($scope.experiments.data[i]);
			}
		});
	
}]);