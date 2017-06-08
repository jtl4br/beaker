angular.module('myApp').factory('CreateExperimentService',
['$timeout', '$http', '$q', function ($timeout, $http, $q) {

    function submit() {
          //Post request to server
          return $http.post('/createExperimentSubmitted',
          {name: name,
            product: product,
            target: target,
            startMonth: startMonth,
            startDay: startDay,
            startYear: startYear,
            endMonth: endMonth,
            endDay, endDay,
            endYear, endYear,
            ageRangeStart: ageRangeStart,
            ageRangeEnd: ageRangeEnd,
            NECheckbox: NECheckbox,
            SECheckbox: SECheckbox,
            MWCheckbox: MWCheckbox,
            NWCheckbox: NWCheckbox,
            SWCheckbox: SWCheckbox,
            iOne: iOne,
            iTwo: iTwo,
            iThree: iThree,
            iFour: iFour,
            iFive: iFive,
            iSix: iSix,
            iSeven: iSeven})
          .success(function(data) {
              return data;
          })
          .error(function(data, status) {
              console.error("Error with create experiment submission", status, data);
          });
      }

      return ({
          submit: submit
      });


}]);
