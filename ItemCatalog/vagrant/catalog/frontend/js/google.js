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
    let data = new FormData();
    data.append('code', authResult['code']);
    data.append('_csrf_token', csrf_token);

    $.ajax({
      type: 'POST',
      url: '/googlesignin',
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      },
      contentType: false,
      success: function(result) {
        window.location.reload(false);
      },
      error: function(xhr, textStatus, errorThrown){
       console.log(xhr);
       console.log(textStatus);
       console.log(errorThrown);
      },
      processData: false,
      data: data
    });
  }
}

$('#signinForm').on('submit', function(event) {
  event.preventDefault();
  var csrf_token = $(this).find("[name='_csrf_token']").val();
  auth2.grantOfflineAccess().then(signInCallback.bind(this, csrf_token));
});

$('#logoutForm').on('submit', function(event) {
  event.preventDefault();
  signOut();
  var csrf_token = $(this).find("[name='_csrf_token']").val();
  let data = new FormData();
  data.append('_csrf_token', csrf_token);

  $.ajax({
    type: 'POST',
    url: '/logout',
    headers: {
      'X-Requested-With': 'XMLHttpRequest'
    },
    contentType: false,
    success: function(result) {
      window.location.reload(false);
    },
    processData: false,
    data: data
  });
});
