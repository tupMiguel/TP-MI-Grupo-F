import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

  matriz: number[][] = [[1, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0]];


  constructor() { }

  ngOnInit(): void {
  }

}
