from grades import main


def test_impossible(capsys, monkeypatch):
    inputs = iter([-1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'impossible!\n'


def test_failed(capsys, monkeypatch):
    inputs = iter([40])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'failed\n'


def test_grade4(capsys, monkeypatch):
    inputs = iter([80])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == '4\n'


def test_incredible(capsys, monkeypatch):
    inputs = iter([102])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert captured.out == 'incredible!\n'
