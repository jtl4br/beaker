angular.module('myApp').controller('viewAllExperimentsController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ($scope, $location, ViewAllExperimentsService) {
		$scope.experiments = null;
		
		ViewAllExperimentsService.getAllExperiments()
			.then(function(data) {
				console.log("ctrl data:"+data);
				$scope.experiments=data;
			});
}]);