import { Component } from '@angular/core';
import { PagamentosPage } from '../pagamentos/pagamentos.page';  // Importe a página que você quer renderizar

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {

  component = PagamentosPage;  // Atribua o componente desejado à propriedade 'component'

  constructor() {}

}
