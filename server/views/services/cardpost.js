app.service("postCardsService",function( $http, $q ) {
    // Return public API.
    return({
        postCards: postCards
    });

            function postCards( playerCards,boardCards ) {

                var request = $http({
                    method: "post",
                    url: "api/index.cfm",
                    data: {
                        playerCards: playerCards,
                        boardCards : boardCards
                    }
                });

                return( request.then( handleSuccess, handleError ) );

            }
                function handleError( response ) {

                    if (
                        ! angular.isObject( response.data ) ||
                        ! response.data.message
                        ) {

                        return( $q.reject( "An unknown error occurred." ) );

                    }

                    // Otherwise, use expected error message.
                    return( $q.reject( response.data.message ) );

                }


                // I transform the successful response, unwrapping the application data
                // from the API response payload.
                function handleSuccess( response ) {

                    return( response.data );

                }

            }
        );
