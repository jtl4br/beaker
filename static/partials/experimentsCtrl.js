angular.module('myApp').controller('experimentsController',
	['$scope', '$location', 'ExperimentsService',
	function ($scope, $location, ExperimentsService) {
		var data = this;
		data.names = [
			{title:'Experiment 1'}
			{title: 'Experiment 2'}
			{title: 'Experiment 3'}];

		data.addData = function() {
			data.names.push({title: data.nameTitle});
			data.nameTitle = '';
		};
}]);