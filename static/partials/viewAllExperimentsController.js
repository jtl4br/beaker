angular.module('myApp').controller('viewAllExperimentsController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ($scope, $location, ViewAllExperimentsService) {
		$scope.data = [
			{id:'1', name:'Experiment 1', product:'gold', start_date:'2017-06-06', end_date:'2017-06-07', active:false},
			{id:'2', name:'Experiment 2', product:'gold', start_date:'2017-06-06', end_date:'2017-06-07', active:true},
			{id:'2', name:'Experiment 3', product:'silver', start_date:'2017-06-06', end_date:'2017-06-07', active:true},
			{id:'2', name:'Experiment 4', product:'gold', start_date:'2017-06-06', end_date:'2017-06-07', active:true},
			{id:'2', name:'Experiment 5', product:'silver', start_date:'2017-06-06', end_date:'2017-06-07', active:true},
			{id:'2', name:'Experiment 6', product:'gold', start_date:'2017-06-06', end_date:'2017-06-07', active:true},
			{id:'3', name:'Experiment 7', product:'platinum', start_date:'2017-06-06', end_date:'2017-06-07', active:false}
		];

		$scope.viewExperiment = function(id) {
			// console.log(id);
			// TODO: Service needs to pull relevant experiment by ID and send to viewExperiment

			// Set the selected experiment in the service
			for (var i = 0, len = $scope.data.length; i < len; i++) {
				if ($scope.data[i].id == id) {
					ViewAllExperimentsService.setSelectedExperiment($scope.data[i]);
				}
			}

			$location.path('/view');
			$location
		}
}]);

	
		//$scope.experiments = [];
		//ViewAllExperimentsService.getAllExperiments().then(function(x){
		//	$scope.experiments = x;
		//	console.log($scope.experiments);
		//	for (var i = 0; i < 2; i++){
		//		console.log($scope.experiments.data[i]);
		//	}
		//});
	
// }]);