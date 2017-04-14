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



function signInCallback(csrf_token, authResult) {
  if (authResult['code']) {

    // $('#signinButton').attr('style', 'display: none');

    let data = new FormData();
    data.append('code', authResult['code'])
    data.append('_csrf_token', csrf_token)

    $.ajax({
      type: 'POST',
      url: '/google-signin',
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      },
      contentType: false,
      success: function(result) {
        // Handle or verify the server response.
      },
      processData: false,
      data: data
    });
  } else {
    // There was an error.
  }
}


$('#signinForm').on('submit', function(event) {
  event.preventDefault()
  var csrf_token = $(this).find("[name='_csrf_token']").val()
  auth2.grantOfflineAccess().then(signInCallback.bind(this, csrf_token));
});


$('#logoutButton').on('click', function(event) {
  signOut()
});
