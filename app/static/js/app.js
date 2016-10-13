var app = angular.module('fma', [
  'ngRoute'
]);

app.config(['$interpolateProvider', function ($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}]);


app.controller('BaseController', function($scope){});
