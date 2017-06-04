

var app = angular.module('PA3',['ui.bootstrap']);
    app.controller('PA3Ctrl',function($scope,$http){

        $scope.heading = "Web Services - PA3";
        $scope.currentPage = 1
        $scope.numPerPage = 10
        $scope.maxSize = 5;
        $scope.ratingValue = 0.0;
        $scope.moreDetails = false;
        $scope.isCollapsed = true;
        $scope.isArray = angular.isArray;
        $scope.tab_pane = "api_tab";
        $scope.signs = ["=","<",">"];
        $scope.selectedSign = $scope.signs[2];
        $scope.filteredData = [];
        $scope.printData = [];
        $scope.mashupData = [];
        $http.get('/getApiData').then(function(response){
            $scope.printData = response.data;
            $scope.totalItems = $scope.printData.length;
        });
        $http.get('/getMashupData').then(function(response){
            $scope.mashupData = response.data;
        });

    $scope.priceRangeFilter = function (selectedSign,ratingValue) {
        return function(row){
            location.rating >= ratingValue;
        }
    };
    $scope.ratingFilter = function (selectedSign,ratingValue) {
        return function(row){
        if(selectedSign == "=")
            return row.rating = ratingValue;
        else if(selectedSign == '>')
            return row.rating > ratingValue;
        else
            return row.rating < ratingValue;
        };
   };


  $scope.pageChanged = function() {
    var begin = (($scope.currentPage - 1) * $scope.numPerPage);
  };
  });
