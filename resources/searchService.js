angular.module('myApp').factory('SearchService',
['$timeout', '$http', function ($timeout, $http, $q) {

    var user = null;

    function getCategory() {
        return $http.get('/api/GetCategory')
        .success(function(data) {
            // console.log(data);
            return data;
        })
        .error(function(data, status) {
            console.error("Error getting categories")
        });
    }

    function getDesignation() {
        return $http.get('/api/GetDesignation')
        .success(function(data) {
            console.log(data);
            return data;
        })
        .error(function(data, status) {
            console.error("Error getting designations")
        });
    }
    function getMajor() {
        return $http.get('/api/GetMajor')
        .success(function(data) {
            // console.log(data);
            return data;
        })
        .error(function(data, status) {
            console.error("Error getting majors")
        });
    }
    function query(title, category, designation, major, year1, type) {
        switch (year1) {
            case 'Freshman':
                year = 1;
                break;
            case 'Sophomore':
                year = 2;
                break;
            case 'Junior':
                year = 3;
                break;
            case 'Senior':
                year = 4;
                break;
            default:
                year = null;
        }

        console.log([title, category, designation, major, year, type]);

        if (type === 'Project') {
            console.log('getting projects...')
            return $http.get('/api/QueryProject', {params:{title:title, category:category, designation:designation, major:major, year:year}})
            .success(function(data) {
                // console.log(data);
            return data;
        })
        .error(function(data, status) {
            console.error("Error getting projects")
        });
        } else if (type === 'Course') {
            return $http.get('/api/QueryCourse', {params:{title:title, category:category, designation:designation}})
            .success(function(data) {
                // console.log(data);
            return data;
        })
        .error(function(data, status) {
            console.error("Error getting courses")
        });
        } else {    //both!
            var xd = [];
            $http.get('/api/QueryProject', {params:{title:title, category:category, designation:designation, major:major, year:year}})
            .success(function(data) {
                // console.log(data);
                xd.push(data);
                $http.get('/api/QueryCourse', {params:{title:title, category:category, designation:designation}})
                .success(function(data) {
                // console.log(data);
                xd.push(data);
                console.log(xd);
                return xd;
                })
                .error(function(data, status) {
                    console.error("Error getting courses")
                });
            })
            .error(function(data, status) {
            console.error("Error getting projects")
            }); 
        }
    }
    return ({
        getCategory: getCategory,
        getDesignation: getDesignation,
        getMajor: getMajor,
        query: query
    });
}]);