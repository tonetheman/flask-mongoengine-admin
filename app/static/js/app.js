var app = angular.module('fma', [
  'ngRoute'
]);

app.config(['$interpolateProvider', '$locationProvider', function ($interpolateProvider, $locationProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');

  $locationProvider.html5Mode({
    enabled: true
  });

}]);
