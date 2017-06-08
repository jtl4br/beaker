angular.module('myApp').controller('viewAllExperimentsController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ($scope, $location, ViewAllExperimentsService) {

		$scope.experiments = [];
		ViewAllExperimentsService.getAllExperiments().then(function(x){
			$scope.experiments = x;
		});

		$scope.viewExperiment = function(id) {
			console.log('viewing exp');
			// TODO: Service needs to pull relevant experiment by ID and send to viewExperiment

			// Set the selected experiment in the service
			for (var i = 0, len = $scope.experiments.data.length; i < len; i++) {
				if ($scope.experiments.data[i].id == id) {
					ViewAllExperimentsService.setSelectedExperiment($scope.experiments.data[i]);
				}
			}
			$location.path('/view');
			$location;
		}
}]);