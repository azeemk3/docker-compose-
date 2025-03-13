function signup() {
    fetch('http://localhost:5000/signup', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        username: document.getElementById('signup_user').value,
        password: document.getElementById('signup_pass').value
      })
    }).then(res => res.json()).then(data => alert(data.message));
  }
  
  function login() {
    fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        username: document.getElementById('login_user').value,
        password: document.getElementById('login_pass').value
      })
    }).then(res => res.json()).then(data => alert(data.message));
  }
  