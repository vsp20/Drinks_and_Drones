import React, { Component } from 'react';
import Item from './Item.js'
import { Button } from 'react-bootstrap';
import coffee from './coffee.png';

//Here we just have to use item as a component and input as many as we need.
// also we implement the shopping cart stuff here( not a component )

class ProductGrid extends Component{
	constructor(props){
		super(props);
		this.addToCart = this.addToCart.bind(this);
		this.state={}
	}
	componentDidMount(){
		// put pull from the shopping cart database here. 

		//set state of shopping cart. 
	}

	addToCart(id){
		alert(id);
	}


	render(){
		return (
			<div className="productGridContainer">
				<div className="itemList">
					<div className="item">
						<Item id="1" name="coffee" imgSrc={coffee}/>
						<Button width="200" height="200" onClick={() => this.addToCart(1)}> Add to Cart </Button>
					</div>
				</div>
				<div className="shoppingCart">
					<div className="title"> Shopping Cart </div>
					<div className="cartBody">
						
					</div>
				</div>
			 </div>
			);
	}
}
export default ProductGrid;