angular.module('myApp').controller('viewExperimentController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ( $scope, $location, ViewAllExperimentsService) {
		$scope.selectedExperiment = ViewAllExperimentsService.getSelectedExperiment();

}]);