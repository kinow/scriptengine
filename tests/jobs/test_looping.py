import yaml

from scriptengine.yaml.parser import parse


def from_yaml(string):
    return parse(yaml.load(string, Loader=yaml.FullLoader))


def test_simple_loop(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: 'Hello {{item}}'
        loop: [1, 2, 3]
    """
    )
    j.run({})
    captured = capsys.readouterr()
    assert "Hello 1" in captured.out
    assert "Hello 2" in captured.out
    assert "Hello 3" in captured.out


def test_loop_in(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: 'Hello {{item}}'
        loop:
            in: [1, 2, 3]
    """
    )
    j.run({})
    captured = capsys.readouterr()
    assert "Hello 1" in captured.out
    assert "Hello 2" in captured.out
    assert "Hello 3" in captured.out


def test_loop_with_in(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: 'Hello {{foo}}'
        loop:
            with: foo
            in: [1, 2, 3]
    """
    )
    j.run({})
    captured = capsys.readouterr()
    assert "Hello 1" in captured.out
    assert "Hello 2" in captured.out
    assert "Hello 3" in captured.out


def test_loop_from_context(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: 'Hello {{item}}'
        loop: '{{loop}}'
    """
    )
    j.run({"loop": [1, 2, 3]})
    captured = capsys.readouterr()
    assert "Hello 1" in captured.out
    assert "Hello 2" in captured.out
    assert "Hello 3" in captured.out


def test_loop_in_dict(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: '{{key}} is {{value}}'
        loop:
            in:
                foo: 1
                bar: 2
                baz: 3
    """
    )
    j.run({})
    captured = capsys.readouterr()
    assert "foo is 1" in captured.out
    assert "bar is 2" in captured.out
    assert "baz is 3" in captured.out


def test_loop_with_in_dict(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: '{{one}} is {{two}}'
        loop:
            with: ['one', 'two']
            in:
                foo: 1
                bar: 2
                baz: 3
    """
    )
    j.run({})
    captured = capsys.readouterr()
    assert "foo is 1" in captured.out
    assert "bar is 2" in captured.out
    assert "baz is 3" in captured.out


def test_loop_in_dict_from_context(capsys):
    j = from_yaml(
        """
        base.echo:
            msg: '{{key}} is {{value}}'
        loop:
            in: '{{dict}}'
    """
    )
    j.run({"dict": {"foo": 1, "bar": 2, "baz": 3}})
    captured = capsys.readouterr()
    assert "foo is 1" in captured.out
    assert "bar is 2" in captured.out
    assert "baz is 3" in captured.out
