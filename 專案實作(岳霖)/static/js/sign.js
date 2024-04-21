function listBtn() {
  var textlistn = document.getElementById('textlistn');
    textlistn.style.display = 'block';
}


const root = document.documentElement;
const eye = document.getElementById('eyeball');
const beam = document.getElementById('beam');
const passwordInput = document.getElementById('password');

root.addEventListener('mousemove', (e) => {
  let rect = beam.getBoundingClientRect();
  let mouseX = rect.right + (rect.width / 2); 
  let mouseY = rect.top + (rect.height / 2);
  let rad = Math.atan2(mouseX - e.pageX, mouseY - e.pageY);
  let degrees = (rad * (20 / Math.PI) * -1) - 350;

  root.style.setProperty('--beamDegrees', `${degrees}deg`);
});


eye.addEventListener('click', e => {
  e.preventDefault();
  document.body.classList.toggle('show-password');
  passwordInput.type = passwordInput.type === 'password' ? 'text' : 'password'
  passwordInput.focus();
});

var checkEye = document.getElementById("checkEye");
      var floatingPassword =  document.getElementById("pass");
      var floatingPassword2 =  document.getElementById("pass2");
      checkEye.addEventListener("click", function(e){
        if(e.target.classList.contains('fa-eye')){
          e.target.classList.remove('fa-eye');
          e.target.classList.add('fa-eye-slash');
          floatingPassword.setAttribute('type','text')
          floatingPassword2.setAttribute('type','text')
        }else{
          floatingPassword.setAttribute('type','password');
          floatingPassword2.setAttribute('type','password');
          e.target.classList.remove('fa-eye-slash');
          e.target.classList.add('fa-eye')
        }
      });

