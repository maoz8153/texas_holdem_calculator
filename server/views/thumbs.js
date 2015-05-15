var app = angular.module('poker', ['ui.bootstrap']);

app.controller('MainCtrl', function($scope, Cards) {
            $scope.formPoker = {
                numberOfPlayers: [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                numberOfBoardCards: 3
            };
            var cardDefault = {
                value: 0,
                shap: '',
                imgLink: '_include/img/work/thumbs/image-02.jpg'
            };


            $scope.playerCards = [];
            $scope.boardCards = [];
            $scope.selected_form = false;
            $scope.select_cards = false;
            $scope.playerCards.push(cardDefault);
            $scope.playerCards.push(cardDefault);
            $scope.updateFormSetting = function(numberOfCards, numberOfPlayer) {
                $scope.selectedNumberOfPlayers = numberOfPlayer;
                $scope.selectedNumberOfCards = numberOfCards;
                $scope.selected_form = true;
                $scope.select_cards = true;
                for (var i = 0; i < numberOfCards; i++) {
                    $scope.boardCards.push(cardDefault);
                }
            };

        })
        app.controller('ModalDemoCtrl', function($scope, $modal, $log, Cards) {
            $scope.items = [
                'item1',
                'item2',
                'item3'
            ];

            $scope.card_display = Cards;
            $scope.animationsEnabled = true;
            $scope.selectedNumberOfPlayers = '';
            $scope.selectedNumberOfCards = '';
            $scope.open = function(size, card) {
                var modalInstance = $modal.open({
                    animation: $scope.animationsEnabled,
                    templateUrl: 'cards_frame.html',
                    windowClass: 'app-modal-window',
                    scope: $scope,
                    controller: 'ModalInstanceCtrl',
                    size: size,
                    resolve: {
                        card_display: function() {
                            return $scope.card_display;
                        }
                    }
                });
                modalInstance.result.then(function(selectedItem) {
                    $scope.selected = selectedItem;
                }, function() {
                    $log.info('Modal dismissed at: ' + new Date());
                });
            };
            $scope.toggleAnimation = function() {
                $scope.animationsEnabled = !$scope.animationsEnabled;
            };
        });
        // Please note that $modalInstance represents a modal window (instance) dependency.
        // It is not the same as the $modal service used above.
        app.controller('ModalInstanceCtrl', function($scope, $modalInstance, card_display, Cards) {
            $scope.card_display.shaps = Cards;
            $scope.card_display = card_display;
            $scope.selected = {
                card_display: $scope.card_display[0]
            };
            $scope.ok = function() {
                $modalInstance.close($scope.selected.card_display);
            };
            $scope.cancel = function() {
                $modalInstance.dismiss('cancel');
            };
        });