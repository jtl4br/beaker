angular.module('myApp').controller('createExperimentController',
	['$scope', '$location', 'CreateExperimentService',
	function ($timeout, $scope, CreateExperimentService) {


	$scope.values = [
	{id: '0', title:"New Customer"},
	{id: '1', title: "Transactions"}
	];

	$scope.selectedTarget = 0;
	
	$scope.postExperiment = function() {

		CreateExperimentService.postExperiment(
			$scope.createExperimentForm.name,
			$scope.createExperimentForm.card,
			$scope.selectedTarget,
			$scope.createExperimentForm.startDate,
			$scope.createExperimentForm.endDate,
			$scope.createExperimentForm.age_l,
			$scope.createExperimentForm.age_u,
			).then(function (data) {
				console.log(data);
			});
		};
}]);