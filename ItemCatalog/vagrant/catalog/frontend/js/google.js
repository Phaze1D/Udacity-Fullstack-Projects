function start() {
  gapi.load('auth2', function() {
    auth2 = gapi.auth2.init({
      client_id: '656484057058-a1shkn8ka0qser9e62nn0m33iobl7nca.apps.googleusercontent.com',
      scope: 'profile email'
    });
  });
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
  });
}



function signInCallback(authResult) {
  if (authResult['code']) {

    // $('#signinButton').attr('style', 'display: none');

    $.ajax({
      type: 'POST',
      url: '/google-signin',
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      },
      contentType: 'application/octet-stream; charset=utf-8',
      success: function(result) {
        // Handle or verify the server response.
      },
      processData: false,
      data: authResult['code']
    });
  } else {
    // There was an error.
  }
}


$('#signinButton').on('click', function(event) {
  auth2.grantOfflineAccess().then(signInCallback);
});


$('#logoutButton').on('click', function(event) {
  signOut()
});
