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
			$location.path('/view');
			$location
		}
}]);

	