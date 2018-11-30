import React, { Component } from 'react';
import Item from './Item.js'
import { Button, FormGroup, FormControl, ControlLabel } from 'react-bootstrap';
import coffee from './coffee.png';
import axios from 'axios';
import { propTypes, reduxForm, Field } from 'redux-form';
import './productGrid.css'
import TextField from 'material-ui/TextField';

//Here we just have to use item as a component and input as many as we need.
// also we implement the shopping cart stuff here( not a component )

const styles = {
    main: {
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
        alignItems: 'center',
        justifyContent: 'center',
    },
    card: {
        minWidth: 300,
    },
    avatar: {
        margin: '1em',
        textAlign: 'center ',
    },
    form: {
        padding: '0 1em 1em 1em',
    },
    input: {
        display: 'flex',
    },
    hint: {
        textAlign: 'center',
        marginTop: '1em',
        color: '#ccc',
    },
};



class ProductGrid extends Component{
	constructor(props){
		super(props);
		this.addToCart = this.addToCart.bind(this);
		this.renderItems = this.renderItems.bind(this);
		this.state={productList: ""};
	}


	componentDidMount(){
		// put pull from the shopping cart database here. 

		//set state of shopping cart. 
		axios.get("http://127.0.0.1:35230/products")
            .then(res=> {
                const data = res.data;
                this.setState({productList: data});
        });
	}

	addToCart(id){
		alert('Item added to cart');
	}

	renderItems(){
		var json = {"coffee":{"name":"coffee","id":"1"},"orange juice":{"name":"orange juice","id":"2"},"strawberry smoothie":{"name":"strawberry smoothie","id":"3"}};
		var arr = [];
		Object.keys(json).forEach(function(key) {
			arr.push(json[key]);
		});
		return <ul>{arr.map(item => <Item id={item.id} name={item.name} imgSrc={coffee}/>)}</ul>;
	}

	handleOrder(){
		//order backend request here
	}

	render(){

		return (
			<div className="productGridContainer">
				<div className="itemList">
					<div className="testing">
					{Object.keys(this.state.productList).map(item => 
						<div className="items">
							<Item id={item.id} name={item} imgSrc={item.img}/>
							<Button bsStyle="info" width="200" height="200" onClick={() => this.addToCart(1)}> Add to Cart </Button>
						</div>
					)}
					</div>
				</div>
				<div className="shoppingCart">
					<h3 className="title"> Shopping Cart </h3>
					<div className="cartBody">
					</div>
				</div>
				<div className="address">
					      <form>
					        <FormGroup
					          controlId="formBasicText"
					        >
					          <ControlLabel>Enter Delivery Address here</ControlLabel>
					          <FormControl
					            type="text"
					            placeholder="1600 Pennsylvania Ave NW, Washington, DC 20500"
					          />
					          <FormControl.Feedback />
					        </FormGroup>
					      </form>
					<Button bsStyle="info">Place Order</Button>
				</div>
			 </div>
			);
	}
}
export default ProductGrid;