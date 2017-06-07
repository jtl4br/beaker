angular.module('myApp').controller('viewAllExperimentsController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ($scope, $location, ExperimentsService) {
		var data = this;
		data.experiments = [
			{id: '1', name:'Experiment 1', product: 'gold', start_date: '2017-06-06', end_date: '2017-06-07', active: false}
			{id: '2', name:'Experiment 2', product: 'gold', start_date: '2017-06-06', end_date: '2017-06-07', active: false}
			{id: '3', name:'Experiment 3', product: 'platinum', start_date: '2017-06-06', end_date: '2017-06-07', active: false}];

		data.addData = function() {
			data.names.push({title: data.nameTitle});
			data.nameTitle = '';
		};
}]);