window.onload = (e) => {
	let cartBtn = document.getElementsByClassName('cartbtn');
	let cartTable = document.querySelector('.cart-tbody');
	let myOffcanvas = document.getElementById('offcanvasScrolling');

	let cartCurrentRow = 0

	for(let btn of cartBtn) {
		btn.onclick = (element) => {
			let product = document.getElementById(`product${btn.value}`);
			let id = document.getElementById(`id${btn.value}`);
			let title = document.getElementById(`t${btn.value}`);
			let price = document.getElementById(`p${btn.value}`);
			let count = document.getElementById(`c${btn.value}`);

			if(!myOffcanvas.classList.contains('show')) {
				myOffcanvas.classList.add('show');
			}


			if(count.innerText - 1 == 0) {
				product.style.display = 'none';
			}

			count.innerText = +count.innerText - 1;
			cartCurrentRow += 1;
			console.log(id.innerText);
			cartTable.innerHTML += `\
			<tr id='r${cartCurrentRow}'>\
			  <input type="number" name="product" value='${+id.innerText}' hidden>\
	          <th scope='row'>${cartCurrentRow}</th>\
	          <td>${title.innerText}</td>\
	          <td>${price.innerText}$</td>\
	          <td>\
	          	<button class='btn btn-outline-danger cartDeleteBtn' type="button" style='font-size: 10px;' id='${cartCurrentRow}' value='${btn.value}'>\
	          		<i class='icon-trash icon-large'></i>\
	          	</button>\
	          </td>\
	        </tr>`;

	        let delBtns = document.getElementsByClassName('cartDeleteBtn');
	        for(let btn of delBtns) {
				btn.onclick = (element) => {
					let row = document.getElementById(`r${btn.id}`);
					let count = document.getElementById(`c${btn.value}`);
					let product = document.getElementById(`product${btn.value}`);

					row.innerHTML = "";
					count.innerText = +count.innerText + 1;

					if(count.innerText == 1) {
						product.style.display = 'block';
					}
				}
			}
		}
	}

	let closeBtn = document.getElementsByClassName('btn-close');
	closeBtn[0].onclick = () => {
		myOffcanvas.classList.remove('show');
	}
}