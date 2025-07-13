/*
main.js
Lógica JavaScript para interactuar con las APIs de análisis léxico y sintáctico.
Estilo Windows 95
*/
document.addEventListener('DOMContentLoaded', () => {
  // Inicializa CodeMirror en el textarea
  const editor = CodeMirror.fromTextArea(document.getElementById('editor'), {
    lineNumbers: true,
    mode: 'javascript',
    theme: 'default',
    lineWrapping: true
  });

  // Función para actualizar la barra de estado
  function updateStatusBar() {
    const cursor = editor.getCursor();
    const statusItems = document.querySelectorAll('.status-item');
    if (statusItems.length >= 3) {
      statusItems[1].textContent = `Línea: ${cursor.line + 1}`;
      statusItems[2].textContent = `Col: ${cursor.ch + 1}`;
    }
  }

  // Actualizar barra de estado cuando el cursor se mueve
  editor.on('cursorActivity', updateStatusBar);
  
  // Actualizar estado inicial
  updateStatusBar();

  // Función para análisis léxico
  async function doLex() {
    const statusItem = document.querySelector('.status-item');
    statusItem.textContent = 'Analizando léxico...';
    
    try {
      const code = editor.getValue();
      const res = await fetch('/api/lex', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ code })
      });
      const tokens = await res.json();
      const tbody = document.querySelector('#tblTokens tbody');
      tbody.innerHTML = '';
      
      tokens.forEach(t => {
        const tr = document.createElement('tr');
        ['type','value','lineno','lexpos'].forEach(f => {
          const td = document.createElement('td');
          td.textContent = t[f];
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
      
      statusItem.textContent = `Listo - ${tokens.length} tokens encontrados`;
    } catch (error) {
      const statusItem = document.querySelector('.status-item');
      statusItem.textContent = 'Error en análisis léxico';
      console.error('Error:', error);
    }
  }

  // Función para análisis sintáctico
  async function doParse() {
    const statusItem = document.querySelector('.status-item');
    statusItem.textContent = 'Analizando sintaxis...';
    
    try {
      const code = editor.getValue();
      const res = await fetch('/api/parse', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ code })
      });
      const data = await res.json();
      const astView = document.getElementById('astView');
      
      if (res.ok) {
        astView.textContent = JSON.stringify(data, null, 2);
        statusItem.textContent = 'Listo - AST generado correctamente';
      } else {
        astView.textContent = `💥 Error de Sintaxis:\n${data.error}`;
        statusItem.textContent = 'Error de sintaxis detectado';
      }
    } catch (error) {
      const statusItem = document.querySelector('.status-item');
      statusItem.textContent = 'Error en análisis sintáctico';
      console.error('Error:', error);
    }
  }

  // Efectos sonoros retro (opcional)
  function playClickSound() {
    // Crear un breve sonido de click estilo Windows 95
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
    
    oscillator.start();
    oscillator.stop(audioContext.currentTime + 0.1);
  }

  // Event listeners con efectos sonoros
  document.getElementById('btnLex').addEventListener('click', () => {
    playClickSound();
    doLex();
  });
  
  document.getElementById('btnParse').addEventListener('click', () => {
    playClickSound();
    doParse();
  });

  // Efectos adicionales para botones
  document.querySelectorAll('.win95-button').forEach(button => {
    button.addEventListener('mousedown', () => {
      button.style.transform = 'translate(1px, 1px)';
    });
    
    button.addEventListener('mouseup', () => {
      button.style.transform = 'none';
    });
    
    button.addEventListener('mouseleave', () => {
      button.style.transform = 'none';
    });
  });

  // Simulación de menú (solo efectos visuales)
  document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', () => {
      playClickSound();
      const statusItem = document.querySelector('.status-item');
      statusItem.textContent = `Menú "${item.textContent}" seleccionado`;
      setTimeout(() => {
        statusItem.textContent = 'Listo';
      }, 2000);
    });
  });

});
