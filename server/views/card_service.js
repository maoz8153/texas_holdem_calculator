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