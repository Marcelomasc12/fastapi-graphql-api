from pathlib import Path
import subprocess


def test_mutacao_fluxo_completo_graphql():
    arquivo = Path("app/graphql_schema.py")

    codigo_original = arquivo.read_text(encoding="utf-8")

    codigo_mutado = codigo_original.replace(
        "posts = db.query(PostModel).all()",
        "posts = []"
    )

    assert codigo_mutado != codigo_original

    try:
        arquivo.write_text(codigo_mutado, encoding="utf-8")

        resultado = subprocess.run(
            ["pytest", "tests/e2e", "-v"],
            capture_output=True,
            text=True
        )
        if resultado.returncode != 0:
            print("\n========== TESTE DE MUTAÇÃO ==========")
            print("Mutação aplicada: GraphQL retorna lista vazia.")
            print("Resultado do E2E: FAILED (esperado)")
            print("Conclusão: O E2E detectou o bug. ✔")
        else:
            print("\n========== TESTE DE MUTAÇÃO ==========")
            print("Mutação aplicada: GraphQL retorna lista vazia.")
            print("Resultado do E2E: PASSED (não esperado)")
            print("Conclusão: O E2E NÃO detectou o bug. ✘")

        assert resultado.returncode != 0

    finally:
        arquivo.write_text(codigo_original, encoding="utf-8")