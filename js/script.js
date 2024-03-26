document.addEventListener('DOMContentLoaded', async function() {
  const tbody = document.querySelector('#body-table');
  const data = await fetch('../data/productos.json');
  const response = await data.json();
  console.log(response);

  let contenidoTableBody = '';

  response.forEach(element => {
    // alt + 96
    contenidoTableBody +=`
      <tr>
        <td>${element.id}</td>
        <td>${element.nombre}</td>
        <td>${element.precio}</td>
        <td>${element.stock}</td>
      </tr>
      
    `;
  })

  console.log(contenidoTableBody);
  tbody.innerHTML = contenidoTableBody;

})