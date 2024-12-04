import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private gerarDocumentoUrl = 'http://localhost:8000/api/gerar-boleto';

  constructor(private http: HttpClient) { }

  // Função para enviar dados no corpo da requisição
  postData(data: any): Observable<any> {
    return this.http.post(this.gerarDocumentoUrl, data);
  }
}
