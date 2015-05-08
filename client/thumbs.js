var app = angular.module('poker',['ui.bootstrap']);


app.factory('Cards', function () {
    var Cards = [];
    var card = {};
    var card_by_shape = [];
    var names = [2,3,4,5,6,7,8,9,'T','J','Q','K','A'];
    var shap  = ['h', 'd', 'c', 's'];
    for (var i = 0; i < shap.length; i++) {
        for (var ii = 0; ii < names.length; ii++) {
            card.names = names[ii];
            card.shap = shap[i];
            card.imgLink = '_' + names[ii] + shap[i] +  '.png' ;
            card_by_shape.push(card);
            card = {};
        }
        Cards.push(card_by_shape);
        card_by_shape = [];
    }
    return  Cards;

    }
);
app.controller('ModalDemoCtrl', function ($scope, $modal, $log, Cards ) {

  $scope.items = ['item1', 'item2', 'item3'];
  $scope.card_display = Cards;
  $scope.animationsEnabled = true;

  $scope.open = function (size) {

    var modalInstance = $modal.open({
      animation: $scope.animationsEnabled,
      templateUrl: 'cards_frame.html',
      windowClass: 'app-modal-window',
      scope : $scope,
      controller: 'ModalInstanceCtrl',
      size: size,
      resolve: {
        items: function () {
          return $scope.items;
        }
      }
    });

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };

  $scope.toggleAnimation = function () {
    $scope.animationsEnabled = !$scope.animationsEnabled;
  };

});

// Please note that $modalInstance represents a modal window (instance) dependency.
// It is not the same as the $modal service used above.

app.controller('ModalInstanceCtrl', function ($scope, $modalInstance, items, Cards) {


    $scope.card_display.shaps = Cards;
  $scope.items = items;
  $scope.selected = {
    item: $scope.items[0]
  };

  $scope.ok = function () {
    $modalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});


app.controller('MainCtrl', function($scope, Cards) {
    $scope.card_display.shaps = Cards;
    $scope.formPoker = {
        numberOfPlayers : 1,
        numberOfBoardCards: 3
    }
    $scope.playerCards = [];
    $scope.boardCards =[];


});
