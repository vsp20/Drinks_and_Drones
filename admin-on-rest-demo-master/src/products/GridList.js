import React from 'react';
import { GridList as MuiGridList, GridTile } from 'material-ui/GridList';
import { NumberField, EditButton } from 'admin-on-rest';
import './gridListStyles.css';
import coffee from './coffee.png';
import RaisedButton from 'material-ui/RaisedButton';
import { Card, CardActions } from 'material-ui/Card';
import { Button } from 'react-bootstrap';

const styles = {
    root: {
        margin: '-2px',
        padding:'10px',
    },
    gridList: {
        width: '100%',
        margin: 0,
    },
};

// For add to cart, every time Add to cart is clicked, the onClick should sent a post request to the backend adding to the cart.
// then in the shopping cart tab, you just show every item that is in the shopping cart. That way the two components don't have to talk


const GridList = ({ ids, isLoading, data, currentSort, basePath, rowStyle }) => (

    <div style={styles.root}>
        <div className="drink" id="1">
            <div className="drinkHeader">
                <div className="drinkTitle">Coffee</div>
            </div>
            <div className="drinkBody">
                <div className="drinkIcon">
                    <img src={coffee} width="200" height="200"/>
                </div>
            </div>
            <Button 
                onClick={
                    function handleClick(){
                        alert('hello');
                    }
                }
            > 
            Add to Cart </Button>
        </div>

    </div>
);

export default GridList;
