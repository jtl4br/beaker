angular.module('myApp').controller('viewAllExperimentsController',
	['$scope', '$location', 'ViewAllExperimentsService',
	function ($scope, $location, ExperimentsService) {
		var data = this;
		data.experiments = [
			{title:'Experiment 1'}
			{title: 'Experiment 2'}
			{title: 'Experiment 3'}];

		data.addData = function() {
			data.names.push({title: data.nameTitle});
			data.nameTitle = '';
		};
}]);